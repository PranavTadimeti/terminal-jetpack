class getCh:

    def __init__(self):
        import sys
        import tty
    
    def __call__(self):
        import sys
        import tty
        import termios 

        fedvar = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fedvar)
        
        try:
            tty.setraw(sys.stdin.fileno())
            charvar = sys.stdin.read(1)
        
        finally:
            termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
        
        return charvar
        