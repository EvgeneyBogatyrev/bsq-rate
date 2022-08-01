from typing import List

import scipy.interpolate

from .exceptions import NoIntersectionError, TooFewLaunchesError


class BSQRate:
    """
    Bitrate-for-the-Same-Quality Rate from MSU Codecs Comparison
    """
    def __init__(self):
        pass

    def score(self, ref_launches: List[dict], test_launches: List[dict], x_key: str, y_key: str) -> float:
        """
        :param ref_launches: reference codec launches
        :param test_launches: test codec launches
        :param x_key: field name for x coordinate
        :param y_key: field name for y coordinate
        :return: score value
        """
        ref_curve, ref_min, ref_max = self.interpolate(ref_launches, x_key, y_key)
        test_curve, test_min, test_max = self.interpolate(test_launches, x_key, y_key)
        x_min = max(ref_min, test_min)
        x_max = min(ref_max, test_max)
        if x_max < x_min:
            raise NoIntersectionError(x_key, ('ref', ref_min, ref_max), ('test', ref_max, test_max))

        ref_auc = ref_curve.integral(x_min, x_max)
        test_auc = test_curve.integral(x_min, x_max)
        return test_auc / ref_auc

    @staticmethod
    def filter_monotonic(launches: List[dict], x_key: str) -> List[dict]:
        """
        Filter launches to meet monotonic restriction on x_key
        Implementation from https://gist.github.com/lovasoa/6733017
        :param launches:
        :param x_key:
        :return: Longest Increasing Subsequence (LIS)
        """
        L = []
        for (k, v) in enumerate(launches):
            L.append(max([L[i] for (i, n) in enumerate(launches[:k]) if n[x_key] < v[x_key]] or [[]], key=len) + [v])
        return max(L, key=len) if L else []

    @staticmethod
    def interpolate(launches: List[dict], x_key: str, y_key: str) -> (scipy.interpolate.UnivariateSpline, float, float):
        """
        Linearly interpolate launches
        :param launches: list of objects
        :param x_key: field name for x coordinate
        :param y_key: field name for y coordinate
        :return: interpolated curve, min_x, max_x
        """
        launches = BSQRate.filter_monotonic(launches, x_key)
        if len(launches) < 2:
            raise TooFewLaunchesError(len(launches))

        x = [launch[x_key] for launch in launches]
        y = [launch[y_key] for launch in launches]
        x_min, x_max = min(x), max(x)
        return scipy.interpolate.UnivariateSpline(x, y, k=1, s=0), x_min, x_max
