from tabulate import tabulate


def format_text(funk):
    def wrapper(*args):
        result = funk(*args)
        return tabulate(
            list(result.items()),
            tablefmt='grid'
        )

    return wrapper
