def create_and_print_grid(rows,cols):
    if not isinstance(rows,int) or not isinstance(cols,int) or rows<=0 or cols<=0:
        print("error , provide  positive integer")
        return
    
    grid_lines=[]
    
    horizontal_segemnt="+---"
    vertical_segment="|   "
    corner="+"
    
    for row_num in range(rows):
        top_line=horizontal_segemnt*cols+corner
        grid_lines.append(top_line)
        
        cell_line=vertical_segment*cols+"|"
        grid_lines.append(cell_line)
        
    bottom_line=horizontal_segemnt*cols+corner
    grid_lines.append(bottom_line)
    
    for line in grid_lines:
        print(line)
        
        
if __name__=="__main__":
    try:
        num_rows=int(input("enter no of rows : \n"))
        num_cols=int(input("enter no of cols:  \n"))
        print("Generate your grid\n")
        create_and_print_grid(num_rows,num_cols)
        
    except ValueError:
        print("\n Invalid input, please enter whole number only")
        
    except Exception as e:
        print(f"An error occurred:{e}")