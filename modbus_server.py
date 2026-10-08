  import asyncio
from pymodbus.server import StartAsyncTcpServer
from pymodbus.simulator import DataType, SimData, SimDevice


async def main():
    device = SimDevice(
        0,
        SimData(
            0,
            datatype=DataType.REGISTERS,
            values=[1234, 5678, 42, 100, 7] + [0] * 95,
        ),
    )
    print("Modbus TCP slave running on 127.0.0.1:502 (Ctrl+C to stop)")
    await StartAsyncTcpServer(context=device, address=("127.0.0.1", 502))


asyncio.run(main())
