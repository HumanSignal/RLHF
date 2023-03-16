def elo_probability(rating1, rating2, k=10):
    """
    Calculate the probability of winning for two players based on their Elo ratings.

    :param rating1: Elo rating of player 1
    :param rating2: Elo rating of player 2
    :param k: scaling factor
    :return: probability of player 1 winning
    """
    prob = 1 / (1 + 10 ** ((rating2 - rating1) / (k * 1.0)))
    return prob


def elo_update(rating, opponent_rating, result, k=32):
    """
    Update the Elo rating for a player based on the result of a game.

    :param rating: player's current Elo rating
    :param opponent_rating: opponent's Elo rating
    :param result: result of the game (1 for win, 0.5 for draw, 0 for loss)
    :param k: scaling factor
    :return: updated Elo rating
    """
    expected_win_probability = elo_probability(rating, opponent_rating, k)
    updated_rating = rating + k * (result - expected_win_probability)
    return updated_rating


def elo_process_comparison_matrix(matrix, initial_rating=1500, k=32):
    n = len(matrix)
    ratings = [initial_rating] * n

    for i in range(n):
        for j in range(i + 1, n):
            result = matrix[i][j]

            if result is not None:
                ratings[i] = elo_update(ratings[i], ratings[j], result, k)
                ratings[j] = elo_update(ratings[j], ratings[i], 1 - result, k)

    # Sort strings by their rating, descending
    sorted_indices = sorted(range(n), key=lambda i: ratings[i], reverse=True)

    return sorted_indices, [ratings[i] for i in sorted_indices]


if __name__ == "__main__":
    # Example usage
    matrix = [
        [None, 1, 0, None],
        [0, None, 1, 1],
        [1, 0, None, 0],
        [None, 0, 1, None]
    ]

    sorted_indices, sorted_ratings = elo_process_comparison_matrix(matrix)

    print("Sorted indices:", sorted_indices)
    print("Sorted ratings:", sorted_ratings)
