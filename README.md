# PYTHON KEYLOGGER SCRIPT

This repository contains a Python script for a keylogger that captures keystrokes and sends them to a Discord channel via a webhook. The script uses the [`pynput`](https://pypi.org/project/pynput/) library to listen for keystrokes and [`requests`](https://pypi.org/project/requests/) to send messages to Discord.

## Features

- Captures keystrokes including special keys like Ctrl, Shift, etc.
- Buffers keystrokes and sends them to Discord in batches of 100.
- Periodically sends any remaining buffered keystrokes every 5 seconds.
- Supports basic formatting for special keys like `[CTRL]`, `[SHIFT]`, etc.

## Prerequisites

### 1. Running Locally

1. **Install Dependencies**: Ensure you have the required Python packages installed:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Webhook URL**: Add your Discord webhook URL to the `.env` file:

   ```env
   WEBHOOK_URL='YOUR_DISCORD_WEBHOOK_URL_HERE'
   ```

3. **Run the Script**

   ```bash
   python keylogger.py
   ```

4. **Stop the Script**: Use `Ctrl + C` to stop the script. It will flush any remaining buffered keystrokes before exiting.

### 2. Running with Docker

1. **Build the Docker Image**

   ```bash
   docker build -t keylogger .
   ```

2. **Run the Docker Container**

   ```bash
   docker run -it --name keylogger keylogger
   ```

## Important Notes

* **Ethical Use**: This script is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Ensure you have explicit permission before running it on any machine.
* **Rate Limits**: Be aware of Discord rate limits. Sending too many messages quickly can cause your webhook to be rate-limited or blocked.
* **Privacy**: Keyloggers capture sensitive data. Use responsibly and securely handle any captured information.

### License

- This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Disclaimer

- The authors are not responsible for any misuse of this code or damage caused.
- Use it at your own risk and comply with all applicable laws and regulations.

### Contact

- For questions or feedback, please open an issue on this repository or contact the maintainer.
