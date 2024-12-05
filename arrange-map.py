from itertools import permutations
import sys

def parse_input():
    """Parse input from standard input."""
    N, M = map(int, input().split())
    grid = [input().split() for _ in range(N)]
    return N, M, grid

def find_sheets(grid, M):
    """Divide the grid into sheets and identify S and D positions."""
    sheets = []
    num_rows, num_cols = len(grid), len(grid[0])
    rows_per_sheet = num_rows // (num_rows // M)
    cols_per_sheet = num_cols // (num_cols // M)

    for r in range(0, num_rows, rows_per_sheet):
        for c in range(0, num_cols, cols_per_sheet):
            sheet = [grid[r_idx][c_idx] for r_idx in range(r, r + rows_per_sheet) 
                     for c_idx in range(c, c + cols_per_sheet)]
            sheets.append(sheet)
    
    return sheets

def find_sd_sheet_indices(sheets):
    """Find indices of sheets containing S and D."""
    s_sheet = next(i for i, sheet in enumerate(sheets) if 'S' in sheet)
    d_sheet = next(i for i, sheet in enumerate(sheets) if 'D' in sheet)
    return s_sheet, d_sheet

def is_valid_placement(prev_sheet, curr_sheet, M):
    """Check if current sheet is valid based on previous sheet."""
    # Convert 1D sheet to 2D
    prev_2d = [prev_sheet[i:i+M] for i in range(0, len(prev_sheet), M)]
    curr_2d = [curr_sheet[i:i+M] for i in range(0, len(curr_sheet), M)]

    # Check right edge of previous sheet connects with left edge of current sheet
    for row in range(M):
        prev_right_edge = [prev_2d[row][M-1]]
        curr_left_edge = [curr_2d[row][0]]
        if prev_right_edge == ['L'] and curr_left_edge == ['L']:
            return False
        if prev_right_edge == ['T'] and curr_left_edge == ['L']:
            return False
        if prev_right_edge == ['L'] and curr_left_edge == ['T']:
            return False

    return True

def bfs_shortest_path(arranged_grid, start, end):
    """Find shortest path between S and D using BFS."""
    rows, cols = len(arranged_grid), len(arranged_grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    # Find start and end coordinates
    sx, sy = next((r, c) for r in range(rows) for c in range(cols) if arranged_grid[r][c] == 'S')
    dx, dy = next((r, c) for r in range(rows) for c in range(cols) if arranged_grid[r][c] == 'D')
    
    queue = [(sx, sy, 0)]
    visited = set([(sx, sy)])
    
    while queue:
        x, y, dist = queue.pop(0)
        
        if x == dx and y == dy:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < rows and 0 <= ny < cols and 
                (nx, ny) not in visited and 
                arranged_grid[nx][ny] in ['T', 'D', 'S']):
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))
    
    return -1  # No path found

def solve_track_laying(N, M, grid):
    """Main solving function."""
    # Find sheets and their indices
    sheets = find_sheets(grid, M)
    s_sheet_idx, d_sheet_idx = find_sd_sheet_indices(sheets)
    
    # Try all permutations of sheets
    remaining_sheets = list(range(len(sheets)))
    remaining_sheets.remove(s_sheet_idx)
    remaining_sheets.remove(d_sheet_idx)
    
    min_distance = float('inf')
    
    # Ensure S sheet is first, D sheet is last
    for perm in permutations(remaining_sheets):
        candidate_order = [s_sheet_idx] + list(perm) + [d_sheet_idx]
        
        # Check if arrangement is valid
        is_valid_arrange = all(
            is_valid_placement(sheets[candidate_order[i]], sheets[candidate_order[i+1]], M)
            for i in range(len(candidate_order)-1)
        )
        
        if is_valid_arrange:
            # Reconstruct grid
            arranged_grid = []
            for i in range(0, len(candidate_order)):
                sheet = sheets[candidate_order[i]]
                sheet_grid = [sheet[j:j+M] for j in range(0, len(sheet), M)]
                
                if i == 0:
                    arranged_grid.extend(sheet_grid)
                else:
                    # Append only the new rows
                    arranged_grid.extend(sheet_grid[len(arranged_grid)//M:])
            
            # Find shortest path
            distance = bfs_shortest_path(arranged_grid, 'S', 'D')
            
            if distance != -1:
                min_distance = min(min_distance, distance)
    
    return min_distance if min_distance != float('inf') else -1

def main():
    """Main function to run the solver."""
    N, M, grid = parse_input()
    result = solve_track_laying(N, M, grid)
    print(result)

if __name__ == "__main__":
    main()