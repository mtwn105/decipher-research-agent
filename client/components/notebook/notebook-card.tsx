"use client";

import Link from "next/link";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Clock, CheckCircle2, AlertCircle, Loader2 } from "lucide-react";
import { DeleteNotebookMenu } from "@/components/notebook/delete-notebook-menu";

type Notebook = {
  id: string;
  title: string | null;
  topic: string | null;
  createdAt: Date;
  updatedAt: Date;
  processingStatus?: {
    status: "IN_QUEUE" | "IN_PROGRESS" | "PROCESSED" | "ERROR";
    message: string | null;
  } | null;
};

type NotebookCardProps = {
  notebook: Notebook;
};

const statusConfig = {
  IN_QUEUE: {
    icon: Clock,
    label: "In Queue",
    variant: "secondary" as const,
  },
  IN_PROGRESS: {
    icon: Loader2,
    label: "Processing",
    variant: "default" as const,
  },
  PROCESSED: {
    icon: CheckCircle2,
    label: "Processed",
    variant: "secondary" as const,
  },
  ERROR: {
    icon: AlertCircle,
    label: "Error",
    variant: "destructive" as const,
  },
};

export function NotebookCard({ notebook }: NotebookCardProps) {
  const status = notebook.processingStatus?.status || "IN_QUEUE";
  const statusInfo = statusConfig[status];
  const StatusIcon = statusInfo.icon;

  return (
    <Link href={`/notebook/${notebook.id}`}>
      <Card className="h-full hover:bg-muted/50 transition-colors p-3 sm:p-4 relative group">
        <CardHeader className="p-0 pb-2">
          <div className="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-1">
            <CardTitle className="text-base sm:text-lg font-semibold line-clamp-2">
              {notebook.title || "Untitled Notebook"}
            </CardTitle>
            <Badge
              variant={statusInfo.variant}
              className="flex items-center gap-1 w-fit text-xs px-2 py-1"
            >
              <StatusIcon className="h-3 w-3" />
              {statusInfo.label}
            </Badge>
          </div>
        </CardHeader>
        <CardContent className="p-0 pb-8">
          {notebook.topic ? (
            <p className="text-xs sm:text-sm text-muted-foreground line-clamp-2 mb-1">
              {notebook.topic}
            </p>
          ) : (
            <p className="text-xs sm:text-sm text-muted-foreground italic mb-1">
              No topic provided
            </p>
          )}
          {notebook.processingStatus?.message && (
            <p className="text-xs text-muted-foreground mt-1 line-clamp-2">
              {notebook.processingStatus.message}
            </p>
          )}
          <p className="text-xs text-muted-foreground mt-2">
            Created on {new Date(notebook.createdAt).toLocaleDateString()}
          </p>
        </CardContent>
        <DeleteNotebookMenu
          notebookId={notebook.id}
          className="absolute bottom-2 right-2 z-10"
        />
      </Card>
    </Link>
  );
}
