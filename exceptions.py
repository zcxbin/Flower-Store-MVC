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
    200006: 'Not found any users',
    200007: 'No user in this day',
    200008: 'No user in this month',
    200009: 'No user in this year',
    200010: 'Not found this bill',
    200011: 'Wrong date type',
    200012: 'No revenue in this date',
    200013: 'Cannot create bill'
}


def raise_error(error_code: int) -> BaseResponse:
    return BaseResponse(
        message=ERROR_CODES.get(error_code),
        status='error',
    )
