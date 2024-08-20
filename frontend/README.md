## Getting Started

First, install:

```bash
pnpm i
```

And run the development server:

```bash
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

# 프로젝트 세팅 Log

## Next.js 설치 (@14.2.5)

```bash
pnpm create next-app@14.2.5 frontend --typescript --tailwind --eslint
```

`frontend` 폴더를 만들고 `typescript`, `tailwind`, `eslint`가 적용된 Next.js 14 프로젝트 초기화

```bash
cd frontend
```

`package.json` 파일 수정

```json
{
  "name": "isteam-ai-calendar",
  "version": "0.1.0",
  "author": {
    "name": "soonbro",
    "email": "tnsgud1110@gmail.com",
    "url": "https://github.com/soonbro/isteam-ai-calendar"
  },
  "private": true
}
```

### Windows

```json
{
  "scripts": {
    "prefastapi-dev": "..\\backend\\.venv\\Scripts\\activate",
    "fastapi-dev": "pip install -q -r ..\\backend\\requirements.txt && python ..\\backend\\main.py",
    "next-dev": "next dev",
    "dev": "concurrently \"pnpm run fastapi-dev\" \"pnpm run next-dev\"",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  }
}
```

### Linux

```json
{
  "scripts": {
    "prefastapi-dev": "..\\backend\\.venv\\Scripts\\activate",
    "fastapi-dev": "pip install -q -r ..\\backend\\requirements.txt && python ..\\backend\\main.py",
    "next-dev": "next dev",
    "dev": "concurrently \"pnpm run fastapi-dev\" \"pnpm run next-dev\"",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  }
}
```

개발환경에서 fastapi 서버와 next dev 서버를 script로 동시에 실행하기 위해 `concurrently` 의존성 추가

```bash
pnpm add concurrently
```

## shadcn/ui 세팅

[shadcn docs - installation next](https://ui.shadcn.com/docs/installation/next)

```bash
pnpm dlx shadcn-ui@latest init
```

> _(Option)_ 설치 할 때, 회사에서 자체 서명 인증서 때문에 TLS 관련 오류 발생 시 무시하고 진행
>
> ```bash
> (.venv) set NODE_TLS_REJECT_UNAUTHORIZED=0
> (.venv) export NODE_TLS_REJECT_UNAUTHORIZED=0
> ```

```bash
✔ Which style would you like to use? › Default
✔ Which color would you like to use as base color? › Neutral
✔ Would you like to use CSS variables for colors? … no / yes
```
