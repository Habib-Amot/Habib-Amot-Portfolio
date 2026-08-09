import io
import pyotp
import base64
import qrcode

code = qrcode.make("ID number: 243222")

memory_obj = io.BytesIO()
code.save(memory_obj, 'png')
print(f"data:img/png;base64 {base64.b64encode(memory_obj.getvalue()).decode()}")

def generate_totp(secret):
    """
    Generate a Time-based One-Time Password (TOTP) using the provided secret.

    Args:
        secret (str): The base32 encoded secret key.
    """
    print(pyotp.totp.TOTP(secret).provisioning_uri(
        name="Amot the dev", issuer_name="Google"
    ))
    return pyotp.totp.TOTP(secret).now()

# print(generate_totp("BAH3A25H5PKMII6P56KWAP326Q243F6T"))