import cv2
import numpy as np

def show_color(b, g, r):
    color = np.zeros((100, 100, 3), dtype=np.uint8)
    color[:] = (b, g, r)
    cv2.imshow("RGB Calculator", color)

def main():
    print("OpenCV RGB Color Calculator")
    print("Enter RGB values (0-255):")
    
    while True:
        try:
            b = int(input("Blue (0-255): "))
            g = int(input("Green (0-255): "))
            r = int(input("Red (0-255): "))
            
            if 0 <= b <= 255 and 0 <= g <= 255 and 0 <= r <= 255:
                show_color(b, g, r)
            else:
                print("Invalid RGB values! Please enter values between 0 and 255.")
        except ValueError:
            print("Invalid input! Please enter integer values.")
        
        # Wait for a key press and close the window if 'q' is pressed
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
