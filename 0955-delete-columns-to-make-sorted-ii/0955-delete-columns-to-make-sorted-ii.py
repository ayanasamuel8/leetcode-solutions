class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        h = len(strs[0])

        processes = [list(range(len(strs)))]

        for i in range(h):
            new_processes = []
            valid = True

            for group in processes:
                for k in range(1, len(group)):
                    if strs[group[k]][i] < strs[group[k - 1]][i]:
                        cnt += 1
                        valid = False
                        break
                if not valid:
                    break

                bucket = defaultdict(list)
                for idx in group:
                    bucket[strs[idx][i]].append(idx)

                for b in bucket.values():
                    if len(b) > 1:
                        new_processes.append(b)

            if valid:
                processes = new_processes

        return cnt