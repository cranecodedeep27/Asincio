import asyncio

# Такие функции называются корутины, т е сопрограммы, которые работают одновременно
async def print1():
    print(1)
    
    
async def print2():
    await asyncio.sleep(10)  # Заглушка какого-либо действия
    print(2)
    

async def print3():
    print(3)
    
    
async def main():
    task1 = asyncio.create_task(print1())
    task2 = asyncio.create_task(print2())
    task3 = asyncio.create_task(print3())
    
    await asyncio.gather(task1, task2, task3)

asyncio.run(main()) # Событийный цикл, т е переключение между задачами

'''Дело в том, что мы не хотим, чтобы остальная программа
ждала выполнения какой-либо части исходной программы'''