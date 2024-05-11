class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        # Dictionary to store points mapped by their maximum coordinate distance from the origin
        max_dist_to_points = collections.defaultdict(list)

        # Fill the dictionary by the maximum distance of each point from the origin
        for point, tag in zip(points, s):
            max_dist = max(abs(point[0]), abs(point[1]))
            max_dist_to_points[max_dist].append((point, tag))

        max_count = 0
        seen_tags = set()

        # Process each possible square size from smallest to largest
        for dist in sorted(max_dist_to_points.keys()):
            current_points = max_dist_to_points[dist]
            current_count = max_count
            unique_tags = True

            # Collect points that can be included in the square without repeating tags
            for point, tag in current_points:
                if tag not in seen_tags:
                    seen_tags.add(tag)
                    current_count += 1
                else:
                    unique_tags = False
                    break

            if unique_tags == False:
                break

            # Update the max_count if the current configuration allows more points
            max_count = max(max_count, current_count)

        return max_count
