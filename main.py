import threading
import detector
import send


def run_detector():
    detector.main()


def run_sender():
    send.main()


if __name__ == "__main__":
    detector_thread = threading.Thread(target=run_detector)
    sender_thread = threading.Thread(target=run_sender)

    detector_thread.start()
    sender_thread.start()

    detector_thread.join()
    sender_thread.join()

