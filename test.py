from latest_fake_useragent import UserAgent


class Test:
    @staticmethod
    def chrome() -> None:
        print('\n--- chrome ---')
        user_agent = UserAgent()
        print(user_agent.latest_versions.chrome)
        for _ in range(100):
            print(user_agent.chrome)

    @staticmethod
    def firefox() -> None:
        print('\n--- firefox ---')
        user_agent = UserAgent()
        for _ in range(100):
            print(user_agent.firefox)


def main() -> None:
    test = Test()
    test.chrome()
    test.firefox()


if __name__ == '__main__':
    main()
