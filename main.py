import argparse

from airtest.core import api

from settings import settings


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        help="spirit||rank||material",
        type=str,
        default="spirit2",
    )
    parser.add_argument(
        "--device",
        help="uuid",
        type=str,
        default=settings.UUID,
    )
    args = parser.parse_args()
    api.init_device(uuid=args.device)
    globals()[args.type]()
