# MIME Protocol Simulation

A minimal Python example demonstrating how to construct a MIME (Multipurpose Internet Mail Extensions) email message with a plain-text body and a file attachment using Python's built-in `email` library.

## What it does

`create_mime.py` builds a multipart email message and prints its raw MIME representation to the console. Specifically, it:

1. Creates a `MIMEMultipart` container with `From`, `To`, and `Subject` headers.
2. Attaches a plain-text body (`MIMEText`).
3. Creates a sample text file (`example.txt`), reads it, Base64-encodes it, and attaches it as an `application/octet-stream` part with a `Content-Disposition: attachment` header.
4. Serializes the full message with `msg.as_string()` and prints it.

The output shows the MIME structure real email clients produce — multipart boundaries, headers, and the Base64-encoded attachment payload.

## Requirements

- Python 3.x (no third-party packages needed; uses only the standard library)

## Usage

```bash
python create_mime.py
```

This prints the assembled MIME message to standard output. To save it to a file instead:

```bash
python create_mime.py > message.eml
```

The resulting `.eml` file can be opened in most email clients.

## Files

| File | Description |
|------|-------------|
| `create_mime.py` | Script that assembles and prints the MIME message. |
| `example.txt` | Sample attachment file (created/overwritten when the script runs). |

## Notes

- The script rewrites `example.txt` on each run with the text `"This is an example attachment."`.
- Sender and recipient addresses are placeholders (`sender@example.com`, `recipient@example.com`); no email is actually sent — the message is only constructed and printed.
- To actually send the message, you would pass `msg.as_string()` to an SMTP client such as Python's `smtplib`.
