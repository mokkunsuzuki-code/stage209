# MIT License © 2025 Motohiro Suzuki
from __future__ import annotations

import pytest

from qsp_demo.protocol import Endpoint, FailClosed
from qsp_demo.wire import Frame, MsgType


def test_happy_path_established():
    c = Endpoint("client")
    s = Endpoint("server")
    c.new_session()

    ch = c.client_hello()
    sh = s.server_recv(ch)
    c.client_recv(sh)

    fin = Frame(version=1, mtype=MsgType.FINISH, session_id=c.session_id, payload=b"fin").encode()
    fin_ack = s.server_recv(fin)
    c.client_recv(fin_ack)

    assert c.state.name == "ESTABLISHED"
    assert s.state.name == "ESTABLISHED"


def test_fail_closed_on_version_mismatch():
    s = Endpoint("server")

    # server INIT で受けるのは CLIENT_HELLO だが version を壊す
    bad = Frame(version=99, mtype=MsgType.CLIENT_HELLO, session_id=b"\x11"*16, payload=b"ch").encode()

    with pytest.raises(FailClosed):
        s.server_recv(bad)

    assert s.state.name == "CLOSED"


def test_fail_closed_on_session_id_mismatch():
    c = Endpoint("client")
    s = Endpoint("server")
    c.new_session()

    ch = c.client_hello()
    sh = s.server_recv(ch)
    c.client_recv(sh)

    bad_sid = b"\x00" * 16
    bad_fin = Frame(version=1, mtype=MsgType.FINISH, session_id=bad_sid, payload=b"fin").encode()

    with pytest.raises(FailClosed):
        s.server_recv(bad_fin)

    assert s.state.name == "CLOSED"
