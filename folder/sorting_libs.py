def get_lib_values():
    lib_score = {}

    for library in problem.libraries:
        time_available = problem.total_steps - problem.step
        if not library.signed:
            time_available = time_available - library.signup_time

        howManyBooks = time_available * library.books_per_day

        lib_score[library.id] = sort_books().head(howManyBooks).sum()

    return lib_score

def sort_books():
    return problem.book_df.assign(f = problem.book_df['bookScores'] * problem.book_df['used']).sort_values('f', ascending=False).drop('f', axis=1)

