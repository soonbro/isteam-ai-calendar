import type { Metadata } from "next";
//import { Inter } from "next/font/google";
import "@/styles/globals.css";
//import "/globals.css";
import { Toaster } from "@/components/ui/sonner";
import { ThemeProvider } from "@/components/theme-provider";

//const inter = Inter({ subsets: ["latin"], variable: "--font-sans" });

export const metadata: Metadata = {
  title: "건설IS팀 AI Calendar 일정 요약 - by.Soonbro",
  description: "롯데건설 IS팀 구글 캘린더 AI 일정 요약",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko">
      <body>
        <ThemeProvider attribute="class" defaultTheme="system">
          <>{children}</>
          {/* <ThemeProvider defaultTheme="system">{children}</ThemeProvider> */}
          <Toaster position="top-left" />
        </ThemeProvider>
      </body>
    </html>
  );
}
