def solution(genres, plays):
    n = len(genres)
    counter = {}
    for i in range(n):
        genre = genres[i]
        play_n = plays[i]
        genre_status = counter.get(genre, {})
        genre_status["cnt"] = genre_status.get("cnt", 0) + play_n
        songs = genre_status.get("songs", {})
        songs[i] = play_n
        genre_status['songs'] = songs
        counter[genre] = genre_status

    answer = []
    sorted_genres = sorted(counter.values(), key=lambda x: -x['cnt'])
    for genre in sorted_genres:
        songs = genre['songs']
        sorted_songs = sorted(list(songs.items()), key=lambda x: (-x[1], x[0]))
        answer += [k for k, v in sorted_songs[:2]]

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
