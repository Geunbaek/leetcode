class Solution:
    def constructDistancedSequence(self, target_number: int) -> List[int]:
        result_sequence = [0] * (target_number * 2 - 1)

        is_number_used = [False] * (target_number + 1)

        self.find_lexicographically_largest_sequence(
            0, result_sequence, is_number_used, target_number
        )

        return result_sequence

    def find_lexicographically_largest_sequence(
        self, current_index, result_sequence, is_number_used, target_number
    ):
        if current_index == len(result_sequence):
            return True

        if result_sequence[current_index] != 0:
            return self.find_lexicographically_largest_sequence(
                current_index + 1,
                result_sequence,
                is_number_used,
                target_number,
            )

        for number_to_place in range(target_number, 0, -1):
            if is_number_used[number_to_place]:
                continue

            is_number_used[number_to_place] = True
            result_sequence[current_index] = number_to_place

            if number_to_place == 1:
                if self.find_lexicographically_largest_sequence(
                    current_index + 1,
                    result_sequence,
                    is_number_used,
                    target_number,
                ):
                    return True
            elif (
                current_index + number_to_place < len(result_sequence)
                and result_sequence[current_index + number_to_place] == 0
            ):
                result_sequence[current_index + number_to_place] = (
                    number_to_place
                )

                if self.find_lexicographically_largest_sequence(
                    current_index + 1,
                    result_sequence,
                    is_number_used,
                    target_number,
                ):
                    return True

                result_sequence[current_index + number_to_place] = 0

            result_sequence[current_index] = 0
            is_number_used[number_to_place] = False

        return False