from asgiref.sync import sync_to_async
from django.shortcuts import render
import asyncio

def landing_page(request):
    return render(request, 'core/landing.html')

async def about_page(request):
        await asyncio.sleep(2)
        return await sync_to_async(render)(request, 'core/about.html')
