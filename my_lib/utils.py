def parse_local_str(vals):
    b = b"".join(v.to_bytes(8, "little") for v in vals)
    return b.rstrip(b"\x00").decode("ascii")
