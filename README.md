# ShopeeFlashBot
"Automate the process of purchasing items during Shopee Flash Sale efficiently using programming techniques and browser configurations"

## Features
- **Flash Sale Monitoring**: Automatically monitors the flash sale page.
- **Automatic Login**: Logs into your Shopee account without manual interaction.
- **Quick Purchase**: Adds items to the cart and completes the checkout process.
- **Bot Detection Bypass**: Uses Undetected Chrome to avoid detection.

## Technologies Used
- **Python**: Main programming language.
- **Selenium**: For browser automation.
- **Chromedriver**: Chrome driver for running the browser.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/bruhismyname/ShopeeFlashBot.git
   cd ShopeeFlashBot
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Download Chromedriver matching your Chrome version from [here](https://sites.google.com/chromium.org/driver/).

4. Place the Chromedriver executable in the project directory.

## Configuration

1. Update `USERAGENT` and `USERDATA` in the code to match your browser settings:
   ```python
   chrome_options.add_argument("user-agent=USERAGENT")  # Replace USERAGENT with your browser's user agent
   chrome_options.add_argument("--user-data-dir=USERDATA")  # Replace USERDATA with your user data directory
   ```

2. Replace `URL_SHOPEE_FLASH_SALE` with the URL of the flash sale page you want to target:
   ```python
   url = "URL_SHOPEE_FLASH_SALE"
   ```

## Usage

1. Run the bot:
   ```bash
   python main.py
   ```

2. Follow the on-screen instructions to handle captchas and other interactions.

3. The bot will automatically:
   - Refresh the page at the specified time.
   - Select product options.
   - Add the item to the cart and proceed to checkout.
   - Choose the preferred payment method (e.g., ShopeePay, COD, or bank transfer).
   - Place the order.

## Notes
- This bot is for educational purposes only. Using bots for shopping may violate Shopee's terms of service.
- Ensure you understand the risks of using automation tools.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements and bug fixes.

## License
This project is licensed under the [MIT License](LICENSE).

## Disclaimer
This project is for educational purposes only. The creator is not responsible for any misuse of this bot.

---

### Contact
For questions or suggestions, reach out via:
- **Email**: [muflihul.aufa@gmail.com](mailto:muflihul.aufa@gmail.com)
- **Instagram**: [mufrajwaa](https://instagram.com/mufrajwaa)
- **GitHub**: [bruhismyname](https://github.com/bruhismyname)
