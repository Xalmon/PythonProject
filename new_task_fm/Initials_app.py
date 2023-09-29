def collect_name():
    return input("Enter your Names: ")


class InitialsApp:

    def split_string(self, full_name):
        name_parts = full_name.split()

        if len(name_parts) == 1:
            return name_parts[0]
        else:
            first_name_initials = ".".join([name[0] for name in name_parts[:-1]])
            initials = f"{first_name_initials} {name_parts[-1]}"
            return initials


# if __name__ == '__main__':
#     app = InitialsApp()
#     full_name = collect_name()
#     result = app.split_string(full_name)
#     print(result)
