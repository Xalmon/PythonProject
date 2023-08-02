language = input('Enter a preferred language : ')
match language:
    case "java":
        print(f'You are a hardcore programmer')
    case "javascript":
        print(f'You are a hardcore programmer')
    case "python":
        print(f'You are a hardcore programmer')
    case _:
        print(f'You are a learner')
