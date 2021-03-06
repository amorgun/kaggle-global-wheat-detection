_base_ = "./universe_r101_gfl_mstrain_local_pseudo.py"

kaggle_working = "/kaggle/working/"
data_root = "/kaggle/input/global-wheat-detection/"
data = dict(
    train=dict(
        ann_file=[
            kaggle_working + "coco_pseudo_test.json",
            kaggle_working + "coco_pseudo_test.json",
            kaggle_working + "coco_pseudo_test.json",
        ],
        img_prefix=[data_root + "test/", data_root + "test/", data_root + "test/"],
    )
)
