from src.bsqrate.bsqrate import BSQRate


ref_launches = [
    {'true_bitrate': 464.1557291666667, 'YUV-SSIM': 0.9243808090686798, 'min_enc_time': 156.64533333333333},
    {'true_bitrate': 811.9263020833333, 'YUV-SSIM': 0.9446667532126108, 'min_enc_time': 190.31733333333335},
    {'true_bitrate': 1452.1744791666667, 'YUV-SSIM': 0.9604259630044302, 'min_enc_time': 236.78466666666668},
    {'true_bitrate': 2792.682552083333, 'YUV-SSIM': 0.9713968833287557, 'min_enc_time': 301.2853333333333},
    {'true_bitrate': 5825.52734375, 'YUV-SSIM': 0.9783317049344381, 'min_enc_time': 398.16833333333335},
    {'true_bitrate': 9667.082291666666, 'YUV-SSIM': 0.9817875425020853, 'min_enc_time': 504.5036666666667}
]
test_launches = [
    {'true_bitrate': 617.5427083333333, 'YUV-SSIM': 0.915120929479599, 'min_enc_time': 28.117666666666665},
    {'true_bitrate': 770.2619791666666, 'YUV-SSIM': 0.9263424475987753, 'min_enc_time': 30.336666666666666},
    {'true_bitrate': 1231.4619791666667, 'YUV-SSIM': 0.9459181030591329, 'min_enc_time': 34.124},
    {'true_bitrate': 1582.05, 'YUV-SSIM': 0.9539503852526346, 'min_enc_time': 36.10866666666667},
    {'true_bitrate': 2779.5921875, 'YUV-SSIM': 0.9668291111787161, 'min_enc_time': 40.161},
    {'true_bitrate': 3881.01171875, 'YUV-SSIM': 0.9715564052263895, 'min_enc_time': 42.129666666666665},
    {'true_bitrate': 8883.016666666666, 'YUV-SSIM': 0.9790446658929189, 'min_enc_time': 48.03133333333333},
    {'true_bitrate': 14052.51484375, 'YUV-SSIM': 0.9826363126436869, 'min_enc_time': 53.443333333333335}
]


def main():
    scorer = BSQRate()
    print(
        'Relative bitrate',
        scorer.score(ref_launches, test_launches, x_key='YUV-SSIM', y_key='true_bitrate')
    )
    print(
        'Relative speed',
        scorer.score(ref_launches, test_launches, x_key='true_bitrate', y_key='min_enc_time')
    )


if __name__ == '__main__':
    main()
