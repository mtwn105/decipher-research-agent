import type { Metadata } from "next";
import { Oxanium } from "next/font/google";
import Script from "next/script";
import "./globals.css";
import { Toaster } from "@/components/ui/sonner";
import { Header } from "@/components/header";
import { Footer } from "@/components/footer";

const oxanium = Oxanium({
  subsets: ["latin"],
});

export const metadata: Metadata = {
  metadataBase: new URL(
    process.env.NEXT_PUBLIC_BASE_URL || "https://decipherit.xyz"
  ),
  title: {
    default:
      "DecipherIt - AI-Powered Research Assistant | Transform Your Research Process",
    template: "%s | DecipherIt",
  },
  description:
    "Transform your research with DecipherIt's AI-powered platform. Upload documents, analyze URLs, generate summaries, create interactive Q&A, audio overviews, visual mindmaps, and FAQs. Bypass geo-restrictions with Bright Data integration.",
  keywords: [
    "AI research assistant",
    "research automation",
    "document analysis",
    "web scraping",
    "AI summaries",
    "interactive Q&A",
    "audio overviews",
    "visual mindmaps",
    "FAQ generation",
    "Bright Data",
    "CrewAI",
    "vector search",
    "knowledge management",
    "research tools",
    "academic research",
    "content synthesis",
    "multi-source research",
    "geo-unrestricted access",
    "NotebookLM alternative",
  ],
  authors: [{ name: "Amit Wani", url: "https://github.com/mtwn105" }],
  creator: "Amit Wani",
  publisher: "DecipherIt",
  category: "Research Tools",
  classification: "AI Research Assistant",
  openGraph: {
    title:
      "DecipherIt - AI-Powered Research Assistant | Transform Your Research Process",
    description:
      "Revolutionary AI research platform inspired by Google NotebookLM. Upload documents, analyze web content, generate summaries, create interactive Q&A, audio overviews, and visual mindmaps. Powered by Bright Data for global web access.",
    type: "website",
    url: "https://decipherit.xyz",
    siteName: "DecipherIt",
    locale: "en_US",
    images: [
      {
        url: "/og.png",
        width: 1200,
        height: 630,
        alt: "DecipherIt - AI-Powered Research Assistant with multi-source analysis, summaries, Q&A, audio overviews, and mindmaps",
        type: "image/png",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    site: "@decipherit",
    creator: "@mtwn105",
    title:
      "DecipherIt - AI-Powered Research Assistant | Transform Your Research Process",
    description:
      "Revolutionary AI research platform. Upload documents, analyze URLs, generate summaries, interactive Q&A, audio overviews & visual mindmaps. Powered by Bright Data & CrewAI.",
    images: ["/og.png"],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  alternates: {
    canonical: "https://decipherit.xyz",
  },
  other: {
    "application-name": "DecipherIt",
    "mobile-web-app-capable": "yes",
    "apple-mobile-web-app-capable": "yes",
    "apple-mobile-web-app-status-bar-style": "default",
    "apple-mobile-web-app-title": "DecipherIt",
    "format-detection": "telephone=no",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${oxanium.className} antialiased`}>
        <Script
          defer
          src="https://mtwnanalytics.xyz/script.js"
          data-website-id="d09597b1-692e-4f54-a378-97e224b7630b"
          strategy="afterInteractive"
        />
        <Header />
        <main className="min-h-screen pt-4">{children}</main>
        <Footer />
        <Toaster />
      </body>
    </html>
  );
}
