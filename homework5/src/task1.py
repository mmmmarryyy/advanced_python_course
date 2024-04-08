import aiohttp
import asyncio
import aiofiles
import os
import sys

async def download_image(session, url, folder_path, image_name):
    async with session.get(url) as response:
        if response.status == 200:
            image_data = await response.read()
            file_path = os.path.join(folder_path, image_name)
            async with aiofiles.open(file_path, 'wb') as file:
                await file.write(image_data)
            print(f"Downloaded {image_name}")

async def download_images(num_images, folder_path):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for i in range(num_images):
            url = f"https://picsum.photos/200/300?random={i}"
            task = asyncio.create_task(download_image(session, url, folder_path, f"image_{i}.jpg"))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    if (len(sys.argv[1:]) < 1):
        print(f"you provide {len(sys.argv[1:])} arguments, 1 expected")
        sys.exit(1)
    
    num_images = int(sys.argv[1])
    folder_path = "../artifacts/5_1/images"
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    asyncio.run(download_images(num_images, folder_path))
