def solution(record):
    result = []
    uid_nick_d = {}
    for r in record:
        cmd, uid, *nickname = r.split()
        if nickname:
            uid_nick_d[uid] = nickname[0]
    for r in record:
        cmd, uid, *nickname = r.split()
        print(cmd, uid, nickname)
        if cmd == 'Enter':
            result.append("{}님이 들어왔습니다.".format(uid_nick_d[uid]))
        elif cmd == 'Leave':
            result.append("{}님이 나갔습니다.".format(uid_nick_d[uid]))
    return result


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

print(solution(record))
