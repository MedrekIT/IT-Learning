#include <SDL2/SDL.h>
#include <SDL2_ttf/SDL_ttf.h>
#include <SDL2_mixer/SDL_mixer.h>
#include <string>
#include <iostream>
#include <cmath>

class Block {
public:
    Block(float xPos, float rectsize, float vel, float mass, float xlimit)
            : x(xPos), y(250), rectsize(rectsize), vel(vel), mass(mass), xlimit(xlimit) {}

    void moveblock() {
        x += vel;
    }

    void drawblock(SDL_Renderer* renderer) {
        float xCon = constrain(x, xlimit);
        SDL_Rect rect = { static_cast<int>(xCon), static_cast<int>(y - rectsize), static_cast<int>(rectsize), static_cast<int>(rectsize) };
        SDL_SetRenderDrawColor(renderer, 150, 150, 150, 255);
        SDL_RenderDrawRect(renderer, &rect);
    }

    void checkcollision(Block& other, Mix_Chunk* clicksound, int& PIAPPROX) {
        if (x <= 0) {
            Mix_PlayChannel(-1, clicksound, 0);
            vel *= -1;
            PIAPPROX++;
        }
        if (x + rectsize >= other.x && x <= other.x + other.rectsize) {
            Mix_PlayChannel(-1, clicksound, 0);
            PIAPPROX++;
            float newVel1 = (mass * vel + other.mass * other.vel + other.mass * (other.vel - vel)) / (mass + other.mass);
            float newVel2 = (other.mass * other.vel + mass * vel + mass * (vel - other.vel)) / (mass + other.mass);
            vel = newVel1;
            other.vel = newVel2;
        }
    }

private:
    float x, y, rectsize, vel, mass, xlimit;

    float constrain(float xPos, float min_val, float max_val = 600) {
        if (xPos < min_val) return min_val;
        if (xPos > max_val) return max_val;
        return xPos;
    }
};

void drawscreen(SDL_Renderer* renderer, TTF_Font* font, Block& block1, Block& block2, int PIAPPROX) {
    SDL_SetRenderDrawColor(renderer, 100, 75, 75, 255);
    SDL_Rect rect = { 0, 250, 600, 50 };
    SDL_RenderFillRect(renderer, &rect);

    block1.drawblock(renderer);
    block2.drawblock(renderer);

    SDL_Color textColor = { 255, 255, 255, 255 };
    std::string text = "Bounces = " + std::to_string(PIAPPROX);
    SDL_Surface* textSurface = TTF_RenderText_Solid(font, text.c_str(), textColor);
    SDL_Texture* textTexture = SDL_CreateTextureFromSurface(renderer, textSurface);
    SDL_Rect textRect = { 0, 250, textSurface->w, textSurface->h };
    SDL_RenderCopy(renderer, textTexture, NULL, &textRect);
    SDL_FreeSurface(textSurface);
    SDL_DestroyTexture(textTexture);
}

int main(int argc, char* argv[]) {
    if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO) < 0) {
        SDL_Log("SDL could not initialize! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }
    if (TTF_Init() == -1) {
        SDL_Log("TTF could not initialize! TTF_Error: %s\n", TTF_GetError());
        return 1;
    }
    if (Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048) < 0) {
        SDL_Log("SDL_mixer could not initialize! Mix_Error: %s\n", Mix_GetError());
        return 1;
    }

    SDL_Window* window = SDL_CreateWindow("Pi approximation by collision", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 600, 300, SDL_WINDOW_SHOWN);
    if (window == nullptr) {
        SDL_Log("Window could not be created! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == nullptr) {
        SDL_Log("Renderer could not be created! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }

    // Use an absolute path for the font file
    TTF_Font* font = TTF_OpenFont("/Users/danielmedrek/Documents/Git public/IT Learning/programming/C++/test/files/times new roman.ttf", 30);
    if (font == nullptr) {
        SDL_Log("Failed to load font! TTF_Error: %s\n", TTF_GetError());
        return 1;
    }

    Mix_Chunk* clicksound = Mix_LoadWAV("/Users/danielmedrek/Documents/Git public/IT Learning/programming/C++/test/files/clack-85854.mp3");
    if (clicksound == nullptr) {
        SDL_Log("Failed to load sound! Mix_Error: %s\n", Mix_GetError());
        return 1;
    }

    int PIAPPROX = 0;

    Block block1(100, 20, 0, 1, 0); // Set a small non-zero velocity for block1
    Block block2(300, 100, -0.1, std::pow(100, 3), 20); // Ensure block2's velocity is correctly set

    bool runWin = true;
    SDL_Event e;
    while (runWin) {
        while (SDL_PollEvent(&e) != 0) {
            if (e.type == SDL_QUIT) {
                runWin = false;
            }
        }

        block1.moveblock();
        block2.moveblock();
        block1.checkcollision(block2, clicksound, PIAPPROX);

        SDL_SetRenderDrawColor(renderer, 50, 50, 75, 255);
        SDL_RenderClear(renderer);

        drawscreen(renderer, font, block1, block2, PIAPPROX);

        SDL_RenderPresent(renderer);
    }

    Mix_FreeChunk(clicksound);
    TTF_CloseFont(font);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    Mix_CloseAudio();
    TTF_Quit();
    SDL_Quit();

    return 0;
}