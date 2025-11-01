import sys
from code_golf_utils.code_golf_utils import load_examples, verify_program

def main():
    if len(sys.argv)!=2:
        print("Usage: python verify_task.py <task_number>  # e.g., 1 for task001")
        raise SystemExit(1)
    n=int(sys.argv[1])
    ex=load_examples(n)           # reads data/taskNNN.json (local)
    verify_program(n, ex)         # auto-loads code/taskNNN.py (local)

if __name__=="__main__":
    main()
