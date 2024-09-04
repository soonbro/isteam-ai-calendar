"use client";

import { ko } from "date-fns/locale";
//import { ChatClient } from "@/chat/chat-client";
import { Button } from "@/components/ui/button";
//import { Skeleton } from "@/components/ui/skeleton";
//import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Calendar } from "@/components/ui/calendar";
import { AnimatedTooltip } from "@/components/ui/animated-tooltip";
//import Image from "next/image";

import { useState } from "react";
import { DateRange } from "react-day-picker";
import Textarea from "@/components/ui/textarea";
import { TextGenerateEffect } from "@/components/ui/text-generate-effect";
import { Skeleton } from "@/components/ui/skeleton";
import { toast } from "sonner";
import { ModeToggle } from "@/components/mode-toggle";

//import ThemeToggle from "@/components/ThemeToggle";

export interface RequestCalendar {
  content: string;
  role: string;
}

export interface RequestSummary {
  model: string;
  content: string;
}

export default function Home() {
  const fromDate = new Date();
  const toDate = new Date().setDate(fromDate.getDate() + 10);
  const [date, setDate] = useState<DateRange | undefined>({
    from: fromDate,
    to: new Date(toDate),
  });

  const [model, setModel] = useState("");
  const [answer, setAnswer] = useState("");
  const [summary, setSummary] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [isSummrizing, setIsSummrizing] = useState(false);
  const [isComplete, setIsComplete] = useState(false);

  const soonbro = [
    {
      id: 1,
      name: "Soonbro",
      designation: "건설IS팀 박순형",
      image: "/soonbro_id_photo.jpg",
    },
  ];

  const handleGetRecentEvent = async () => {
    setIsLoading(true);
    const response = await fetch("/api/get_recent_event");
    if (!response.ok) {
      setIsLoading(false);
      toast(
        `HTTP Error! - status: ${response.status} (${response.statusText})`
      );
      //throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    setIsLoading(false);
    return data.events;
  };

  const onSummaryEvent = async (model: string, answer: string) => {
    setIsSummrizing(true);
    setIsComplete(false);
    console.log(answer);
    const response = await fetch("/api/summary", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: model,
        question: answer,
      }),
    });
    console.log(answer);
    if (!response.ok) {
      toast(`HTTP error! status: ${response.status}`);
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    setSummary(data.answer);
    setIsSummrizing(false);
    setIsComplete(true);
  };

  const onButtonClick = async () => {
    if (model == "") {
      toast("언어 모델을 선택해주세요!", {
        description: "OpenAI 또는 Ollama LLM 모델을 선택해주세요.",
      });
      return;
    }
    setAnswer("향후 10일간의 일정입니다.");
    console.log("event - 일정 요약 버튼 클릭");
    const answer = await handleGetRecentEvent();
    setAnswer(answer);
    console.log(answer);
    if (answer) {
      await onSummaryEvent(model, answer);
    }
    return;
  };

  return (
    <main className="flex min-h-screen flex-col items-center px-10 bg-bg dark:bg-secondaryBlack overflow-hidden">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <p className="fixed left-0 top-0 flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-6 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit dark:text-darkText lg:static lg:w-[320px] lg:justify-between lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-darkBg font-mono font-bold">
          건설IS팀 AI Calendar 일정 요약
          {/*<ThemeToggle />*/}
        </p>

        <div className="fixed bottom-0 left-0 flex h-24 w-full mt-4 overflow-visible items-end justify-center bg-gradient-to-t from-white via-white dark:from-black dark:via-black lg:static lg:size-auto lg:bg-none">
          <div className="flex flex-row place-items-center gap-0 lg:p-0">
            <a
              className="pointer-events-none lg:pointer-events-auto flex place-items-center gap-2 p-8"
              href="https://github.com/soonbro/isteam-ai-calendar"
              target="_blank"
              rel="noopener noreferrer"
            >
              <span className="dark:text-white select-none none">{"By "}</span>
              <em className="bg-main dark:text-black">Soonbro</em>
              <div className="flex flex-row items-center justify-center w-full">
                <AnimatedTooltip items={soonbro} />
              </div>
            </a>
            <ModeToggle />
          </div>
        </div>
      </div>
      <div className="flex w-full max-w-5xl justify-stretch mt-2 m650:flex-col sm:flex-col md:flex-row">
        <div className="flex flex-col space-y-4 w-full max-w-5xl mt-20 lg:mt-5 m650:items-center sm:items-start">
          <div className="flex space-x-1 items-end">
            <Select onValueChange={setModel}>
              <SelectTrigger className="bg-neutral-300 w-[180px]">
                <SelectValue placeholder="Select AI Model" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectLabel className="text-zinc-700 select-none">
                    *** OpenAI ***
                  </SelectLabel>
                  <SelectItem value="gpt-4o">GPT4o 🥇💸</SelectItem>
                  <SelectItem value="gpt-4o-mini">GPT4o-mini 🏅</SelectItem>
                  <SelectLabel className="text-zinc-700 select-none">
                    *** Ollama ***
                  </SelectLabel>
                  <SelectItem value="llama3">llama3:7b 🔤</SelectItem>
                  <SelectItem value="EEVE">EEVE:10.8b</SelectItem>
                  <SelectItem value="Gemma2">Gemma2:9b</SelectItem>
                  <SelectItem value="qwen2">Qwen2:7b</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
            <Button className="font-bold" onClick={onButtonClick}>
              일정 요약
            </Button>
          </div>

          <Calendar
            className="hidden md:block"
            mode="range"
            selected={date}
            onSelect={setDate}
            locale={ko}
          />
        </div>
        {/*<Textarea className="min-h-[480px] m-4" spellCheck="false" />*/}
        <Textarea
          className="rounded-base min-h-[370px] mt-4 md:mt-20 lg:mt-4 border-2 border-border dark:border-darkBorder bg-main p-4 shadow-light dark:shadow-dark"
          value={answer}
          setValue={setAnswer}
          placeholder=""
          spellCheck={false}
        />
      </div>
      {isLoading ? (
        <TextGenerateEffect
          words="구글 캘린더에서 건설IS팀 일정을 불러오고 있습니다..."
          className="flex flex-col items-center w-full"
        />
      ) : (
        <>
          {isSummrizing ? (
            <>
              <TextGenerateEffect
                words="AI가 일정을 요약하고 있습니다..."
                className="flex flex-col items-center w-full"
              />
              <Skeleton className="flex flex-col w-full max-w-5xl rounded-base min-h-[400px] mt-4 mb-12 bg-neutral-400" />
            </>
          ) : (
            <>
              {isComplete ? (
                <Textarea
                  className="max-w-5xl rounded-base h-[80vh] mt-4 mb-12 border-2 border-border dark:border-darkBorder bg-mainAccent p-4 shadow-light dark:shadow-dark"
                  value={summary}
                  setValue={setSummary}
                  placeholder=""
                  spellCheck={false}
                />
              ) : (
                <></>
              )}
            </>
          )}
        </>
      )}
      <div className="bottom-0 left-0 mt-auto mb-auto flex flex-col w-full items-center justify-center ">
        <b>🚧 Disclaimer 🚧</b>
        <li>
          본 페이지는{" "}
          <u>
            <b>AI CoP</b> 과정에서 LLM 및 LangChain 학습을 목표로 개발
          </u>{" "}
          중이며, 가장 기본적인 기능 구현만 된 상태입니다.
        </li>
      </div>
    </main>
  );
}
