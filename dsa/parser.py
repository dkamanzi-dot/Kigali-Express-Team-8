import xml.etree.ElementTree as ET
import re


def extract_transaction(sms, index):
    body = sms.attrib.get("body", "")
    readable_date = sms.attrib.get("readable_date", "")

    # Find transaction ID
    id_match = re.search(
        r"(?:Financial Transaction Id|TxId):\s*(\d+)",
        body,
        re.IGNORECASE
    )

    if id_match:
        transaction_id = id_match.group(1)
    else:
        # Some messages do not contain a transaction ID,
        # so create a unique ID based on the SMS position.
        transaction_id = f"SMS-{index}"

    # Find amount
    amount_patterns = [
        r"payment of ([\d,]+) RWF",
        r"received ([\d,]+) RWF",
        r"transferred ([\d,]+) RWF",
        r"withdrawn ([\d,]+) RWF",
        r"transaction of ([\d,]+) RWF",
        r"deposit of ([\d,]+) RWF"
    ]

    amount = 0

    for pattern in amount_patterns:
        amount_match = re.search(pattern, body, re.IGNORECASE)

        if amount_match:
            amount = int(amount_match.group(1).replace(",", ""))
            break

    # Determine transaction type
    body_lower = body.lower()

    if "payment of" in body_lower:
        transaction_type = "payment"
    elif "transferred" in body_lower:
        transaction_type = "transfer"
    elif "received" in body_lower:
        transaction_type = "received"
    elif "withdrawn" in body_lower:
        transaction_type = "withdrawal"
    elif "bank deposit" in body_lower or "deposit" in body_lower:
        transaction_type = "deposit"
    elif "transaction of" in body_lower:
        transaction_type = "transaction"
    else:
        transaction_type = "other"

    # Extract sender / receiver
    sender = None
    receiver = None

    received_match = re.search(
        r"received [\d,]+ RWF from (.+?) \(",
        body,
        re.IGNORECASE
    )

    transfer_match = re.search(
        r"transferred [\d,]+ RWF to (.+?) \(",
        body,
        re.IGNORECASE
    )

    payment_match = re.search(
        r"payment of [\d,]+ RWF to (.+?) \d+ has",
        body,
        re.IGNORECASE
    )

    if received_match:
        sender = received_match.group(1).strip()

    elif transfer_match:
        receiver = transfer_match.group(1).strip()

    elif payment_match:
        receiver = payment_match.group(1).strip()

    return {
        "id": transaction_id,
        "type": transaction_type,
        "amount": amount,
        "sender": sender,
        "receiver": receiver,
        "timestamp": readable_date
    }


def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    sms_records = root.findall("sms")

    transactions = []

    for index, sms in enumerate(sms_records, start=1):
        transaction = extract_transaction(sms, index)
        transactions.append(transaction)

    return transactions


if __name__ == "__main__":
    transactions = parse_xml("data/modified_sms_v2-1.xml")

    print("Number of SMS records:", len(transactions))

    print("\nFirst transaction:")
    print(transactions[0])

    print("\nSecond transaction:")
    print(transactions[1])
