# Keylogger Script

This repository contains a Python script for a keylogger that captures keystrokes and sends them to a Discord channel via a webhook. The script uses the `pynput` library to listen for keystrokes and the `requests` library to send messages to Discord.

## Features

- Captures keystrokes including special keys.
- Buffers keystrokes and sends them to Discord in batches of 100.
- Periodically sends any remaining buffered keystrokes every 5 seconds.
- Supports basic key formatting for special keys.

## Prerequisites

Before running the script, ensure you have the following Python packages installed:

- `requests`
- `pynput`

You can install these packages using `pip`:

```bash
pip install requests pynput
```

## Configuration

1. **Webhook URL**: Replace the placeholder webhook URL in the script with your actual Discord webhook URL:

    ```python
    WEBHOOK_URL = 'YOUR_DISCORD_WEBHOOK_URL_HERE'
    ```

2. **Buffer Size and Interval**: The buffer size is set to 100 keystrokes, and the script sends messages every 5 seconds. You can adjust these values if needed.

## Usage

1. **Run the Script**: Execute the script using Python:

    ```bash
    python keylogger.py
    ```

2. **Stop the Script**: To stop the script, use Ctrl+C in the terminal where it is running. The script will flush any remaining buffered keystrokes before exiting.

## Important Notes

- **Ethical Use**: This script is intended for educational purposes only. Unauthorized use of keyloggers can be illegal and unethical. Ensure you have explicit permission to run this script on any machine.
- **Rate Limits**: Be mindful of Discord rate limits. Sending too many messages in a short period may result in your webhook being rate-limited or blocked.
- **Privacy**: Be cautious with handling sensitive information. Keyloggers can capture personal and confidential data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

The authors of this script do not take responsibility for any misuse of the code. Use it at your own risk and ensure you comply with all relevant laws and regulations.

## Contact

For any questions or feedback, please open an issue on the repository or contact the repository maintainer.
