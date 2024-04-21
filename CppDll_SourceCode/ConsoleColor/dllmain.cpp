// dllmain.cpp : Defines the entry point for the DLL application.
#include "3rdparty/console-color.hpp"
#include <Windows.h>
#include <iostream>
using namespace std;
#define EXTERNC extern "C"
#define DLL_EXPORT __declspec(dllexport) //For Calling Python DLL Functions

EXTERNC DLL_EXPORT void Printfviacolor(const char* txt, int r, int g, int b) {
    cs::color_string cscolor(txt);
    cscolor.use(cs::color::color(r, g, b));
    cout << cscolor << endl;
}
BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

