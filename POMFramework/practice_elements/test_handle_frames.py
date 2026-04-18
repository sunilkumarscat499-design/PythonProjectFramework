from playwright.sync_api import Page, expect

def test_frames(page:Page):
    # page.goto("https://ui.vision/demo/webtest/frames/")

    '''this is single frame locator '''
    # frame = page.frame_locator("frame[src='frame_1.html']")
    # frame.locator("[type='text']").fill("Hello")
    # page.wait_for_timeout(5000)

    '''this is nested frame locator '''
    # frame = page.frame(url = "https://ui.vision/demo/webtest/frames/frame_3.html")
    # child_frame = frame.child_frames
    # print(child_frame)
    # frame2 = child_frame[0]
    # frame2.get_by_label("I am a human").click()
    # page.wait_for_timeout(5000)


    '''Excersece'''

    page.goto("https://demo.automationtesting.in/Frames.html")
    page.get_by_text("Iframe with in an Iframe").click()
    frame = page.frame(url="https://demo.automationtesting.in/MultipleFrames.html")
    child_frame = frame.child_frames[0]
    child_frame.locator("input[type='text']").fill("Iframe practice")
    page.wait_for_timeout(5000)


