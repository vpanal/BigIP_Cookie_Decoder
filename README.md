# BigIP_Cookie_Decoder

This script decodes BigIP cookies in the format `Name:1677787402.36895.0000` or `1677787402.36895.0000` and displays the resulting IP address and port.

## Installation

To install this project, follow these steps:

1. Clone the repository from GitHub using the following command:

```bash
git clone http://github.com/vpanal/BigIP_Cookie_Decoder
```

2. Navigate to the project directory:

```bash
cd BigIP_Cookie_Decoder
```

3. Install the required dependencies using `pip` and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Once these steps are completed, the project will be ready to use. If you're using a virtual environment, make sure to activate it before running the `pip install` command. If you don't have `git` installed, you can download the repository code in ZIP format from the link: http://github.com/vpanal/BigIP_Cookie_Decoder/archive/main.zip

## Usage

You can use this script in four different ways:

1. **Interactive mode for a single cookie:** Run the script without arguments (`python bigip_decoder.py`) to manually input cookies. The program will prompt you to enter a cookie in the format `Name:1677787402.36895.0000` or `1677787402.36895.0000`. The script will decode it and terminate.

2. **Interactive mode:** Run the `--interactive` option. The program will prompt you to enter a cookie in the format `Name:1677787402.36895.0000` or `1677787402.36895.0000`. Enter "quit" or "exit" to exit the interactive mode.

3. **Provide a single cookie:** Use the `-c` or `--cookie` option to directly provide a single cookie in the command line.

   Example:
   ```
   python bigip_decoder.py -c Name:1677787402.36895.0000
   ```

4. **Read cookies from a file:** Use the `-i` or `--input-file` option to provide a file containing cookies in the format `Name:1677787402.36895.0000` or `1677787402.36895.0000`.

   Example:
   ```
   python bigip_decoder.py -i input.txt
   ```

## Examples

### Example 1: Interactive mode for a single Cookie

Run the script without arguments (`python bigip_decoder.py`) to manually input cookies:

```
python bigip_decoder.py
Enter a cookie in the format Name:1677787402.36895.0000 or 1677787402.36895.0000.
Enter the cookie: lala:1677787402.36895.0000
lala-10.1.1.100:8080
```

### Example 2: Interactive mode

Use the `--interactive` option to manually input cookies in interactive mode:

```
python bigip_decoder.py --interactive
Interactive mode. Enter a cookie in the format Name:1677787402.36895.0000 or 1677787402.36895.0000, or type 'quit' or 'exit' to exit.
Enter the cookie: lala:1677787402.36895.0000
lala-10.1.1.100:8080
Enter the cookie: 1677787402.36895.0000
Cookie-10.1.1.100:8080
Enter the cookie: quit
```

### Example 3: Provide a single cookie

Use the `-c` or `--cookie` option to provide a single cookie directly in the command line:

```
python bigip_decoder.py -c lala:1677787402.36895.0000
lala-10.1.1.100:8080

python bigip_decoder.py -c 1677787402.36895.0000
Cookie-10.1.1.100:8080
```

### Example 4: Read cookies from a file

Use the `-i` or `--input-file` option to provide a file containing cookies in the format `Name:1677787402.36895.0000` or `1677787402.36895.0000`:

Contents of `input.txt`:
```
srv1:1677787402.36895.0000
srv2:1677787402.36895.0000
1677787402.36895.0000
srv3:1677787402.36895.0000
srv4:1677787402.36895.0000
srv5:1677787402.36895.0000
```

Run the script:

```
python bigip_decoder.py -i input.txt
--- Decoded IPs ---

srv1-10.1.1.100:8080
srv2-10.1.1.100:8080
Cookie-10.1.1.100:8080
srv3-10.1.1.100:8080
srv4-10.1.1.100:8080
srv5-10.1.1.100:8080

--------------------------
```

## Requirements

This script requires Python 3 and the `argparse` module.

## References

- [Overview of BIG-IP Persistence Cookie Encoding](https://my.f5.com/manage/s/article/K6917)

## Authors

- [vpanal](https://github.com/vpanal): Pentester.

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/). You can find more information in the [LICENSE](LICENSE) file.
