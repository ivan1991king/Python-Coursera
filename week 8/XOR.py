print(
    *list(
        map(
            lambda x, y: x^y,
            map(
                int, input().split()
            ),
            map(
                int, input().split()
            )
        )
    )
)