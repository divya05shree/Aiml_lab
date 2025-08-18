def find_points_in_grid(grid):
    start_point=None
    task_points=[]
    
    
    for y, row in enumerate(grid):
        for x,char in enumerate (row):
            if char =='S':
                start_point=(x,y)
            elif char=='T':
                task_points.append((x,y))           
    return start_point,task_points


def main():
    print("enter your ASCII grid.print enter after grid entered")
    grid_lines=[]
    while True:
        try:
            line=input()
            if not line:
                break
            grid_lines.append(line)
        except EOFError:
            break
        
    if not grid_lines:
        print("\n No grid Enterd")
        
    start,tasks=find_points_in_grid(grid_lines)
    print("\n-----grid results---\n")
    
    if start:
        print(f"Start 'S' found at coordinates:{start}" )
        
    else:
        print("Start 'S' not found in the grid")
    
    
    if tasks:
        print(f"Found {len(tasks)} task(S) 'T' at coordinates :{tasks}")
        
    else:
        print("No tasks 'T' were found in the grid")
        
    print("---------")
    
    
if __name__=="__main__":
    main()