import os
from platane_snk import generate_snake

def main():
    os.makedirs("dist", exist_ok=True)  # Ensure the 'dist' directory exists
    generate_snake(github_user_name="thisissagarthapa", output_path="dist/github-contribution-grid-snake.svg")

if __name__ == "__main__":
    main()
