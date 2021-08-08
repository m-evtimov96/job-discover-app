import os
import magic
from django.core.exceptions import ValidationError


def validate_is_doc(file):
    valid_mime_types = ['application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/pdf']
    file_mime_type = magic.from_buffer(file.read(2048), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Unsupported file type. Use docx or pdf ')
    valid_file_extensions = ['.docx', '.pdf']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unacceptable file extension. Use .docx or .pdf')


def file_size(value):
    limit = 2 * 1024 * 1024
    if value:
        if value.size > limit:
            raise ValidationError('File too large. Size should not exceed 2 MB.')
