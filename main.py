from app import VideoScanApp


if __name__ == "__main__":
    app = VideoScanApp()
    user_input_path = input(
        "Please input the directory path to scan for video files: "
    ).strip()
    print("Starting directory scan & database processing...")
    app.execute_and_save_to_db(user_input_path)
