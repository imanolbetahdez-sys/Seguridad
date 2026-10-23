"""
Genera un certificado autofirmado (certificado.crt) y su llave privada (llave.key)
compatibles con Python 3.13 (VERIFY_X509_STRICT).

Requisito:  pip install cryptography

Uso:
    python generar_certificado.py                  -> usa 192.168.10.1
    python generar_certificado.py 192.168.10.1     -> IP del servidor
"""
import ipaddress
import sys
from datetime import datetime, timedelta, timezone

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID

IP_SERVIDOR = sys.argv[1] if len(sys.argv) > 1 else '192.168.10.1'
DIAS_VALIDEZ = 365

# 1. Llave privada
llave = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# 2. Datos del certificado (emisor = sujeto porque es autofirmado)
nombre = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, 'MX'),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, 'Ciberseguridad'),
    x509.NameAttribute(NameOID.COMMON_NAME, IP_SERVIDOR),
])

# 3. SAN: la IP del servidor (el cliente valida contra esto) + localhost para pruebas
san = [x509.IPAddress(ipaddress.ip_address(IP_SERVIDOR))]
if IP_SERVIDOR != '127.0.0.1':
    san.append(x509.IPAddress(ipaddress.ip_address('127.0.0.1')))
san.append(x509.DNSName('localhost'))

ahora = datetime.now(timezone.utc)
certificado = (
    x509.CertificateBuilder()
    .subject_name(nombre)
    .issuer_name(nombre)
    .public_key(llave.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(ahora - timedelta(minutes=5))
    .not_valid_after(ahora + timedelta(days=DIAS_VALIDEZ))
    .add_extension(x509.SubjectAlternativeName(san), critical=False)
    .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
    .add_extension(
        x509.KeyUsage(
            digital_signature=True, key_encipherment=True, key_cert_sign=True,
            content_commitment=False, data_encipherment=False, key_agreement=False,
            crl_sign=False, encipher_only=False, decipher_only=False,
        ),
        critical=True,
    )
    .add_extension(
        x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]), critical=False
    )
    .add_extension(
        x509.SubjectKeyIdentifier.from_public_key(llave.public_key()), critical=False
    )
    .add_extension(
        x509.AuthorityKeyIdentifier.from_issuer_public_key(llave.public_key()),
        critical=False,
    )
    .sign(llave, hashes.SHA256())
)

# 4. Guardar archivos
with open('llave.key', 'wb') as f:
    f.write(llave.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

with open('certificado.crt', 'wb') as f:
    f.write(certificado.public_bytes(serialization.Encoding.PEM))

huella = certificado.fingerprint(hashes.SHA256()).hex(':').upper()
print(f'Certificado generado para la IP {IP_SERVIDOR} (valido {DIAS_VALIDEZ} dias)')
print('  - certificado.crt  -> copiar al SERVIDOR y al CLIENTE')
print('  - llave.key        -> SOLO en el SERVIDOR (nunca compartir)')
print(f'Huella SHA-256: {huella}')
