from schemas.base_response import BaseResponse

ERROR_CODES = {
    100001: 'Login failed!',
    100002: 'Credentials are not correct!',
    100003: 'Register failed!',
    200001: 'Get all flowers failed!',
    200002: 'Create flower failed!',
    200003: 'Create bill failed',
    200004: 'Do not have this account',
    200005: 'Not found this flower',
    200008: 'Not found this bill'
}


def raise_error(error_code: int) -> BaseResponse:
    return BaseResponse(
        message=ERROR_CODES.get(error_code),
        status='error',
    )
