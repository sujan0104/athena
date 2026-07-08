from athena.core.application import AthenaApplication


def main() -> None:
    app = AthenaApplication()
    raise SystemExit(app.run())


if __name__ == "__main__":
    main()
