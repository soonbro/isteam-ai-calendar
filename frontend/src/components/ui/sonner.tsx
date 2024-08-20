"use client";

import { useTheme } from "next-themes";
import { Toaster as Sonner } from "sonner";

type ToasterProps = React.ComponentProps<typeof Sonner>;

const Toaster = ({ ...props }: ToasterProps) => {
  const { theme = "system" } = useTheme();

  return (
    <Sonner
      theme={theme as ToasterProps["theme"]}
      className="toaster group"
      toastOptions={{
        classNames: {
          toast:
            "group toast group-[.toaster]:bg-main group-[.toaster]:text-black group-[.toaster]:text-sm group-[.toaster]:rounded-base group-[.toaster]:border-2 group-[.toaster]:border-border dark:group-[.toaster]:border-darkBorder group-[.toaster]:shadow-light dark:group-[.toaster]:shadow-dark",
          description:
            "group-[.toast]:text-secondaryBlack group-[.toast]:text-xs",
          actionButton:
            "group-[.toast]:bg-primary group-[.toast]:text-primary-foreground",
          cancelButton:
            "group-[.toast]:bg-muted group-[.toast]:text-muted-foreground",
        },
      }}
      {...props}
    />
  );
};

export { Toaster };
