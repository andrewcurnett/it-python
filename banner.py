def banner(title, author):
    title_length = len(title)
    byline = f"By {author}"
    byline_length = len(byline)
    banner_length = max(title_length, byline_length) + 8

    print("=" * (banner_length+2))
    print(f"{title:^{banner_length}}")
    print(f"{byline:^{banner_length}}")
    print("_" * (banner_length+2))
    print("")

banner("BANNER", "Andrew Curnett")
name = input("What is your name? ")
title = input("What is the quest? ")
print("")
banner(title, name)
